function removeMsg(msg) {
    $(msg).parent().remove();
}

$(document).ready(() => {
    setTimeout(() => {
        $('.alter-dismissible').fadeOut('fast');
    }, 5000);
});
