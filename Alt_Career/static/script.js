
function validateForm() {
    // document.getElementById('job-form').submit()
    // return true
    let _skill1 = document.getElementById('skill1-choice')
    let _skill2 = document.getElementById('skill2-choice')
    let _skill3 = document.getElementById('skill3-choice')
    let _skill4 = document.getElementById('skill4-choice')
    let _skill5 = document.getElementById('skill5-choice')
    let _skill6 = document.getElementById('skill6-choice')
    let _skill7 = document.getElementById('skill7-choice')

    let skill1 = JSON.parse(document.getElementById('skill1-list').innerHTML)
    let skill2 = JSON.parse(document.getElementById('skill2-list').innerHTML)
    let skill3 = JSON.parse(document.getElementById('skill3-list').innerHTML)
    let skill4 = JSON.parse(document.getElementById('skill4-list').innerHTML)
    let skill5 = JSON.parse(document.getElementById('skill5-list').innerHTML)
    let skill6 = JSON.parse(document.getElementById('skill6-list').innerHTML)
    let skill7 = JSON.parse(document.getElementById('skill7-list').innerHTML)

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

    if (skill6.includes(_skill6.value)) {
        if (_skill6.classList.contains('error')) {
            _skill6.classList.remove('error')
        }
    } else {
        _skill6.classList.add('error')
        success = false
    }

    if (skill7.includes(_skill7.value)) {
        if (_skill7.classList.contains('error')) {
            _skill7.classList.remove('error')
        }
    } else {
        _skill7.classList.add('error')
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
    console.log(tagName)
    let dataOptions = ""
    options.forEach(option => {
        let optionHTML = `<option value="${option}">${option}</option>\n`
        dataOptions += optionHTML;
    });
    tag.innerHTML = dataOptions;
}

window.onload = () => {
    fetch(`/skills`)
        .then(response => response.json())
        .then(data => {
            populateSelect(`skill1-datalist`, data['data'])
            document.getElementById(`skill1-list`).innerHTML = JSON.stringify(data['data']);
        })
}

function loadSkills(event) {
    let caller = event.target.id.split('-')[0]
    let s7 = document.getElementById('skill7-choice').value
    let s6 = document.getElementById('skill6-choice').value
    let s5 = document.getElementById('skill5-choice').value
    let s4 = document.getElementById('skill4-choice').value
    let s3 = document.getElementById('skill3-choice').value
    let s2 = document.getElementById('skill2-choice').value
    let s1 = document.getElementById('skill1-choice').value
    let url = `/${caller}?`
    switch (caller) {
        case 'skill7': url += 'skill7=' + s7
        case 'skill6': url += 'skill6=' + s6 + '&'
        case 'skill5': url += 'skill5=' + s5 + '&'
        case 'skill4': url += 'skill4=' + s4 + '&'
        case 'skill3': url += 'skill3=' + s3 + '&'
        case 'skill2': url += 'skill2=' + s2 + '&'
        case 'skill1': url += 'skill1=' + s1 + '&'
    }
    url += 'dummy=d'
    fetch(url)
        .then(response => response.json())
        .then(data => {
            let c = parseInt(caller[caller.length - 1])
            populateSelect(`skill${c + 1}-datalist`, data['data'])
            document.getElementById(`skill${c + 1}-list`).innerHTML = JSON.stringify(data['data']);
        })

}
