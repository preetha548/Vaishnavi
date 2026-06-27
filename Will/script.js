function downloadPDF() {
    window.print();
}

function enableEdit() {

    const inputs = document.querySelectorAll("input");

    inputs.forEach(input=>{
        input.removeAttribute("readonly");
    });

    alert("Form is editable.");
}