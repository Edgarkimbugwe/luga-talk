const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_text");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const slug = "{{ blogpost.slug }}"; // Pass the slug from Django template

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


// Attach click event listeners to all edit buttons
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        // Retrieve the comment ID from the clicked button's data attribute
        let commentId = e.target.getAttribute("data-comment_id");
        // Get the current content of the comment using its ID
        let commentContent = document.getElementById(`comment${commentId}`).innerText;

        // Populate the comment text area with the current comment content
        commentText.value = commentContent;
        // Change the submit button text to indicate updating action
        submitButton.innerText = "Update";
        // Set the form action to the edit comment URL with the comment ID
        commentForm.setAttribute("action", `/${slug}/edit_comment/${commentId}`);
    });
}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        e.preventDefault();
        let commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `/${slug}/delete_comment/${commentId}`;
        deleteModal.show();
    });
}