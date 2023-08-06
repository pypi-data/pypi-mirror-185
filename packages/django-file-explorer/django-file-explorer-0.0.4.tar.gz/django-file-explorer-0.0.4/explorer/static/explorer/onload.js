window.onload = function() {
    correctActionBtn();
    correctVolumeList();
};

function correctVolumeList(){
    // GETTING VOLUME LIST
    let vol_list = document.getElementsByName('volume-list');

    // LOOPING THROUGH EACH VOLUME
    for (let vol of vol_list){        
        // GETTING SELETECTED CLASS
        selected = getVolumeSelectClass(vol.id);

        // GETTING ENABLE CLASS
        enable = getVolumeEnableClass(vol.id);

        // GETTING TITLE INFO
        title = getTitleInfo(vol.id)

        // UPDATING CLASS
        vol.className += ` ${selected} ${enable}`;
        
        // UPDATING TITLE
        vol.title = title;
    }
}

function correctActionBtn(){
    // GETTING LIST OF ALL BUTTON
    let action_btn = document.getElementsByName('action-btn');

    // GETTING COLOR CLASSES
    const color_classes = {
        'download': 'btn-primary',
        'delete': 'btn-danger',
        'upload': 'btn-warning',
    };
    for (let btn of action_btn){
        // GETING ACTION NAME
        action = btn.id;

        // CHAINING TEXT
        let action_str = capitalizeFirstLetter(action);
        btn.innerHTML = action_str;

        // CHAINING COLOR
        btn_color = color_classes[action];
        if (btn_color != undefined){
            btn.className += ` ${btn_color}`;
            btn.title = `${action_str} data`
        }else {
            btn.title = 'Action color not defined'
        }
    }
}