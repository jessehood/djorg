(function() {
  class Bookmarks { 
    constructor() {
      this.deleteLinks = Array.from(document.getElementsByClassName('delete-link'));
  
      this.deleteLinks.forEach(link => this.attachConfirmationEvent(link));
    }
  
    /**
     * Adds a confirmation dialog event to an anchor link that deletes a bookmark.
     * @param {Element} deleteLink
     */
    attachConfirmationEvent(deleteLink) {
      deleteLink.addEventListener('click', function confirmDelete(event) {
        const bookmarkName = this.getAttribute('data-name');
        const confirmResult = confirm(`Are you sure you want to delete your ${bookmarkName} bookmark?`);

        if (!confirmResult) {
          event.preventDefault();
        }
      });
    }
  }

  new Bookmarks();
})();


