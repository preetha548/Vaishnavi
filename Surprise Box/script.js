const fields = [
    ["name","showName"],
    ["destination","showDestination"],
    ["date","showDate"],
    ["time","showTime"],
    ["message","showMessage"]
];

fields.forEach(item=>{

    const input=document.getElementById(item[0]);
    const output=document.getElementById(item[1]);

    input.addEventListener("input",()=>{

        output.textContent=input.value;

    });

});
