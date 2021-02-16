
function validateForm() {
    // document.getElementById('job-form').submit()
    // return true
    let _industry = document.getElementById('industry-choice')
    let _functionalArea = document.getElementById('functionalArea-choice')
    let _skill1 = document.getElementById('skill1-choice')
    let _skill2 = document.getElementById('skill2-choice')
    let _skill3 = document.getElementById('skill3-choice')
    let _skill4 = document.getElementById('skill4-choice')
    let _skill5 = document.getElementById('skill5-choice')

    let functionalArea = JSON.parse(document.getElementById('functionalAreas-list').innerHTML)
    let skill1 = JSON.parse(document.getElementById('skill1-list').innerHTML)
    let skill2 = JSON.parse(document.getElementById('skill2-list').innerHTML)
    let skill3 = JSON.parse(document.getElementById('skill3-list').innerHTML)
    let skill4 = JSON.parse(document.getElementById('skill4-list').innerHTML)
    let skill5 = JSON.parse(document.getElementById('skill5-list').innerHTML)

    let success = true

    if (skill1.includes(_skill1.value)) {
        if (_skill1.classList.contains('error')) {
            _skill1.classList.remove('error')
        }
    } else {
        _skill1.classList.add('error')
        success = false
    }

    if (skill2.includes(_skill2.value)) {
        if (_skill2.classList.contains('error')) {
            _skill2.classList.remove('error')
        }
    } else {
        _skill2.classList.add('error')
        success = false
    }

    if (skill3.includes(_skill3.value)) {
        if (_skill3.classList.contains('error')) {
            _skill3.classList.remove('error')
        }
    } else {
        _skill3.classList.add('error')
        success = false
    }

    if (skill4.includes(_skill4.value)) {
        if (_skill4.classList.contains('error')) {
            _skill4.classList.remove('error')
        }
    } else {
        _skill4.classList.add('error')
        success = false
    }

    if (skill5.includes(_skill5.value)) {
        if (_skill5.classList.contains('error')) {
            _skill5.classList.remove('error')
        }
    } else {
        _skill5.classList.add('error')
        success = false
    }
    console.log(success)

    if (success) {
        document.getElementById('job-form').submit()
    } else {
        window.alert('Please select the closest value that applies to you from the suggestions')
    }

}


function populateSelect(tagName, options) {
    let tag = document.getElementById(tagName)
    let dataOptions = ""
    options.forEach(option => {
        let optionHTML = `<option value="${option}">${option}</option>\n`
        dataOptions += optionHTML;
    });
    tag.innerHTML = dataOptions;
}
