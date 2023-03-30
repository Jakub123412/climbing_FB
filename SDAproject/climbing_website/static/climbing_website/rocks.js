function scrollAndClick(testId) {
    if (testId == null) {
        return;
    }
    const element = document.getElementById(`rock_${testId}`)
    const button = element.querySelector('button')
    button.click()

    $('html, body').animate({
        scrollTop: $(element).offset().top
    }, 500);
}