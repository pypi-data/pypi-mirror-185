
function enableAllActionBtn(){
    // GETTING LIST OF ALL BUTTON
    let action_btn = document.getElementsByName('action-btn');

    // LOOPING THROUGH EACH BUTTON
    for (let btn of action_btn){
        btn.disabled = false;
    }
}

function diableAllActionBtn(){
    // GETTING LIST OF ALL BUTTON
    let action_btn = document.getElementsByName('action-btn');

    // LOOPING THROUGH EACH BUTTON
    for (let btn of action_btn){
        btn.disabled = true;
    }
}

function getHiddneField(name, value){
    let s = document.createElement("input");
    s.setAttribute("type", "hidden");
    s.setAttribute("value", value);
    s.setAttribute("name", name);
    // s.setAttribute("id", `form-${name}`)
    return s;
}

function removeField(field_name){
    var fields = document.getElementsByName(field_name);
    while(fields.length != 0){
        console.log(`in loop -> ${field_name}`);
        // REMOVING
        for (const field of fields){
            field.remove();
        }
        
        // CHECKING CONDITION AGAIN
        fields = document.getElementsByName(field_name);
    }
}

function formValueUpdate(action){
    // GETTING FORM
    const form = document.getElementById('actionform');

    // REMOVE ALL HIDEEN FIELDS IF EXISTS
    removeField('volume');
    removeField('action');
    removeField('check_idx');
    removeField('location');

    // ADDING ACTION FIELD
    let hf = getHiddneField("action", action)
    form.append(hf);

    // ADDING CHECKBOX IDX
    for (let check_idx of selected_idx){
        let hf = getHiddneField("check_idx", `${check_idx}`)
        form.append(hf);
    }

    // GETTING URL INFORMATION
    let url = window.location.href;
    url = url.split('?');
    url = url[url.length -1];

    // GETTING REQUEST PARAMETERS
    let parameters = url.split('&');
    for (let parameter of parameters){
        // GETTING KEY AND VALUE
        let psplit = parameter.split('=');
        let k = psplit[0];
        let v = psplit[psplit.length - 1];

        // GETTING CORRECT VALUE
        if (psplit.length == 1){
            v = null;
        }

        // ADDING HIDDEN FIELDS
        let hf = getHiddneField(k, v)
        form.append(hf);
        // console.log(`${k}:${v}`)
    }

    // ADDING VOLUME INFORMATION
    vol_name = getSelectedVolume();
    try {
        document.getElementById('form-volume').value = vol_name;
    } catch (error) {
        // ADDING HIDDEN FIELDS
        let hf = getHiddneField('volume', vol_name)
        form.append(hf);
        // console.log(error);
    }
}