document.addEventListener("DOMContentLoaded", () => {
    const seasonFilter = document.querySelector('select[name="season"]');
    if (seasonFilter) {
        seasonFilter.addEventListener("change", () => {
            seasonFilter.form.submit();
        });
    }

    const addToCartButtons = document.querySelectorAll(".btn-primary");
    addToCartButtons.forEach(button => {
        button.addEventListener("click", () => {
            alert("Item added to cart!");
        });
    });
});
