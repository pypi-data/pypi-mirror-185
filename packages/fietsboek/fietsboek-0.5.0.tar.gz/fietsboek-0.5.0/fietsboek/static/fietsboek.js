/**
 * Installs a listener to the given DOM objects.
 *
 * @param selector - The query selector to find the DOM objects.
 * @param event - The event name to listen to.
 * @param handler - The handler function.
 */
function addHandler(selector, event, handler) {
  document.querySelectorAll(selector).forEach((obj) => obj.addEventListener(event, handler));
}

/**
 * Handler for when a tag is clicked. Removes the tag from the tag list.
 *
 * @param event - The triggering event.
 */
function tagClicked(event) {
  const span = event.target.closest('span');
  span.parentNode.removeChild(span);
}

addHandler(".tag-badge", "click", tagClicked);

/**
 * Handler to add a new tag when the button is pressed.
 */
function addTag() {
  const newTag = document.querySelector("#new-tag");
  if (newTag.value === "") {
    return;
  }
  const node = document.createElement("span");
  node.classList.add("tag-badge");
  node.classList.add("badge");
  node.classList.add("rounded-pill");
  node.classList.add("bg-info");
  node.classList.add("text-dark");
  node.addEventListener("click", tagClicked);
  const text = document.createTextNode(newTag.value);
  node.appendChild(text);
  const icon = document.createElement("i");
  icon.classList.add("bi");
  icon.classList.add("bi-x");
  node.appendChild(icon);
  const input = document.createElement("input");
  input.hidden = true;
  input.name = "tag[]";
  input.value = newTag.value;
  node.appendChild(input);
  document.querySelector("#formTags").appendChild(node);
  const space = document.createTextNode(" ");
  document.querySelector("#formTags").appendChild(space);
  newTag.value = "";
}

addHandler("#add-tag-btn", "click", addTag);
// Also add a tag when enter is pressed
addHandler("#new-tag", "keypress", (event) => {
  if (event.keyCode == 13) {
    event.preventDefault();
    addTag();
  }
});

/**
 * Function to check for password validity.
 *
 * @param main - The actual entered password.
 * @param repeat - The repeated password, must match `main`.
 */
function checkPasswordValidity(main, repeat) {
  const mainPassword = document.querySelector(main);
  const repeatPassword = document.querySelector(repeat);

  const form = mainPassword.closest('form');
  form.classList.remove('was-validated');

  // Check password requirements. The validation errors are not actually
  // displayed, as the HTML template contains pre-filled texts for that.
  if (mainPassword.value.length != 0 && mainPassword.value.length < 8) {
    mainPassword.setCustomValidity('Too short');
  } else {
    mainPassword.setCustomValidity('');
  }

  if (mainPassword.value != repeatPassword.value) {
    repeatPassword.setCustomValidity('Needs to match');
  } else {
    repeatPassword.setCustomValidity('');
  }
}

// This function is used via a HTML onchange= handler, so make eslint happy
checkPasswordValidity;

/**
 * Function to check for name validity.
 *
 * @param name - The name that should be checked.
 */
function checkNameValidity(name) {
  const nameField = document.querySelector(name);
  if (nameField.value.length == 0) {
    nameField.setCustomValidity('Needs a name');
  }
}

// This function is used via a HTML onchange= handler, so make eslint happy
checkNameValidity;

/**
 * Hit the endpoint to search for friends. This populates the friend selector
 * when tagging friends.
 */
function searchFriends() {
  const searchPattern = document.querySelector("#friendSearchQuery").value.toLowerCase();
  const friendSearch = document.querySelector("#friendSearch");
  friendSearch.innerHTML = "";
  fetch(FRIENDS_URL)
    .then((response) => response.json())
    .then((response) => {
      const blueprint = document.querySelector("#friendSearchBlueprint");

      // Only show friends with a matching name
      const friends = response.filter((obj) => obj.name.toLowerCase().indexOf(searchPattern) != -1);

      friends.forEach((friend) => {
        const copy = blueprint.cloneNode(true);
        copy.removeAttribute("id");
        copy.querySelector(".friend-name").textContent = friend.name;
        copy.querySelector("button").addEventListener("click", (event) => {
          const button = event.target.closest("button");
          button.parentNode.parentNode.removeChild(button.parentNode);

          const added = document.querySelector("#friendAddedBlueprint").cloneNode(true);
          added.removeAttribute("id");
          added.querySelector(".friend-name").textContent = friend.name;
          added.querySelector("input").value = friend.id;
          added.querySelector("input").removeAttribute("disabled");
          added.querySelector("button").addEventListener("click", removeFriendClicked);
          document.querySelector('#taggedFriends').appendChild(added);
        });
        friendSearch.appendChild(copy);
      });
    });
}

addHandler("#add-friend-btn", "click", () => searchFriends());
// Also trigger the search on Enter keypress
addHandler("#friendSearchQuery", "keypress", (event) => {
  if (event.keyCode == 13) {
    event.preventDefault();
    searchFriends();
  }
});

/**
 * Handler for when a "Remove friend" button is clicked.
 *
 * @param event - The triggering event.
 */
function removeFriendClicked(event) {
  const button = event.target.closest("button");
  button.parentNode.parentNode.removeChild(button.parentNode);
}

addHandler(".remove-friend-button", "click", removeFriendClicked);

/**
 * Handler for when the image input is changed.
 *
 * This handler splits the multiple images up into single input fields, such
 * that each one can be removed individually. It also adds preview images, and
 * adds the button to delete and edit the image's description.
 *
 * @param event - The triggering event.
 */
function imageSelectorChanged(event) {
  for (const file of event.target.files) {
    window.fietsboekImageIndex++;

    const input = document.createElement("input");
    input.type = "file";
    input.hidden = true;
    input.name = `image[${window.fietsboekImageIndex}]`;

    const transfer = new DataTransfer();
    transfer.items.add(file);
    input.files = transfer.files;

    const preview = document.querySelector("#trackImagePreviewBlueprint").cloneNode(true);
    preview.removeAttribute("id");
    preview.querySelector("img").src = URL.createObjectURL(file);
    preview.querySelector("button.delete-image").
      addEventListener("click", deleteImageButtonClicked);
    preview.querySelector("button.edit-image-description").
      addEventListener("click", editImageDescriptionClicked);
    preview.querySelector("input.image-description-input").
      name = `image-description[${window.fietsboekImageIndex}]`;
    preview.appendChild(input);

    document.querySelector("#trackImageList").appendChild(preview);
  }

  event.target.value = "";
}

addHandler("#imageSelector", "change", imageSelectorChanged);

/**
 * Handler to remove a picture from a track.
 *
 * @param event - The triggering event.
 */
function deleteImageButtonClicked(event) {
  const preview = event.target.closest("div.track-image-preview");
  /* If this was a image yet to be uploaded, simply remove it */
  const input = preview.querySelector("input[type=file]");
  if (input) {
    preview.parentNode.removeChild(preview);
    return;
  }

  /* Otherwise, we need to remove it but also insert a "delete-image" input */
  const deleter = preview.querySelector("input.image-deleter-input");
  deleter.removeAttribute("disabled");
  preview.removeChild(deleter);
  preview.parentNode.appendChild(deleter);
  preview.parentNode.removeChild(preview);
}

addHandler("button.delete-image", "click", deleteImageButtonClicked);

/**
 * Handler to show the image description editor.
 *
 * @param event - The triggering event.
 */
function editImageDescriptionClicked(event) {
  window.fietsboekCurrentImage = event.target.closest("div");

  const currentDescription = event.target.
    closest("div").querySelector("input.image-description-input").value;
  const modalDom = document.getElementById("imageDescriptionModal");
  modalDom.querySelector("textarea").value = currentDescription;

  const modal = bootstrap.Modal.getOrCreateInstance(modalDom, {});
  modal.show();
}

addHandler("button.edit-image-description", "click", editImageDescriptionClicked);

/**
 * Handler to save the image description of the currently edited image.
 *
 * @param event - The triggering event.
 */
function saveImageDescriptionClicked(event) {
  const modalDom = document.getElementById("imageDescriptionModal");
  const wantedDescription = modalDom.querySelector("textarea").value;
  window.fietsboekCurrentImage.
    querySelector("input.image-description-input").value = wantedDescription;
  window.fietsboekCurrentImage.
    querySelector("img").title = wantedDescription;

  const modal = bootstrap.Modal.getOrCreateInstance(modalDom, {});
  modal.hide();

  window.fietsboekCurrentImage = undefined;
}

addHandler("#imageDescriptionModal button.btn-success", "click", saveImageDescriptionClicked);

/**
 * Handler to toggle (collapse/expand) the yearly/monthly summary.
 *
 * @param event - The triggering event.
 */
function toggleSummary(event) {
  const chevron = event.target;
  const containing = chevron.closest("a");
  const summary = containing.nextElementSibling;
  bootstrap.Collapse.getOrCreateInstance(summary).toggle();
  if (chevron.classList.contains("bi-chevron-down")) {
    chevron.classList.remove("bi-chevron-down");
    chevron.classList.add("bi-chevron-right");
  } else {
    chevron.classList.remove("bi-chevron-right");
    chevron.classList.add("bi-chevron-down");
  }
}

addHandler(".summary-toggler", "click", toggleSummary);

/*
 * Handler to enable the "Download archive button" ...
 */
addHandler("#archiveDownloadButton", "click", () => {
  const checked = document.querySelectorAll(".archive-checkbox:checked");
  const url = new URL("/track/archive", window.location);
  checked.forEach((c) => {
    url.searchParams.append("track_id[]", c.value);
  });
  window.location.assign(url);
});
/*
 * ... and the listeners on the checkboxes to disable and enable the button.
 */
addHandler(".archive-checkbox", "change", () => {
  const checked = document.querySelectorAll(".archive-checkbox:checked");
  document.querySelector("#archiveDownloadButton").disabled = (checked.length == 0);
});

/**
 * Handler to clear the input when a .button-clear-input is pressed.
 *
 * The button must be in an input-group with the input.
 *
 * @param event - The triggering event.
 */
function clearInputButtonClicked(event) {
  event.target.closest(".input-group").querySelectorAll("input").forEach((i) => i.value = "");
  event.target.closest(".input-group").querySelectorAll("select").forEach((i) => i.value = "");
}

addHandler(".button-clear-input", "click", clearInputButtonClicked);


document.addEventListener('DOMContentLoaded', function() {
  window.fietsboekImageIndex = 0;

  /* Enable tooltips */
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map((tooltipTriggerEl) => {
    return new bootstrap.Tooltip(tooltipTriggerEl, {sanitize: false});
  });

  /* Enable Bootstrap form validation */
  const forms = document.querySelectorAll('.needs-validation');
  Array.from(forms).forEach((form) => {
    form.addEventListener('submit', (event) => {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }

      form.classList.add('was-validated');
    }, false);
  });

  /* Format all datetimes to the local timezone */
  document.querySelectorAll(".fietsboek-local-datetime").forEach((obj) => {
    const timestamp = obj.attributes["data-utc-timestamp"].value;
    const date = new Date(timestamp * 1000);
    const intl = new Intl.DateTimeFormat(LOCALE, {dateStyle: "medium", timeStyle: "medium"});
    obj.innerHTML = intl.format(date);
  });
});
