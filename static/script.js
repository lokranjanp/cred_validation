document.addEventListener("DOMContentLoaded", function () {
    const generateForm = document.getElementById("generate-form");
    const validateForm = document.getElementById("validate-form");

    if (generateForm) {
        generateForm.addEventListener("submit", function (event) {
            const prefixInput = document.getElementById("prefix");
            const lengthInput = document.getElementById("length");

            const prefix = prefixInput.value;
            const length = parseInt(lengthInput.value, 10);

            if (isNaN(length) || length <= 0) {
                alert("Length must be a positive number.");
                event.preventDefault();
                return;
            }

            if (!/^\d+$/.test(prefix)) {
                alert("Prefix must be a numeric value.");
                event.preventDefault();
            }
        });
    }

    if (validateForm) {
        validateForm.addEventListener("submit", function (event) {
            const numberInput = document.getElementById("number");

            if (!/^\d+$/.test(numberInput.value)) {
                alert("Number must be a numeric value.");
                event.preventDefault();
            }
        });
    }
});
