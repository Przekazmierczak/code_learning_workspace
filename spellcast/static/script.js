// Function to remove highlighting from elements
function remove_highlight() {
    const darkElements = document.querySelectorAll('.highlight_dark');
    const lightElements  = document.querySelectorAll('.highlight_light');
    const allElements = Array.from(darkElements).concat(Array.from(lightElements))
    
    allElements.forEach((element) => {
        element.classList.remove('highlight_dark', 'highlight_light');
    });
}

// Function to copy values to special blocks
function copy_special_block_value() {
    for (let i = 1; i < 26; i++) {
        const input_name = 'special_block_' + i;
        const input = document.querySelector('input[name="' + input_name + '"]');
        
        const values = ['normal_block', 'double_letter', 'triple_letter', 'double_points'];

        values.forEach(function(value){
            if (input.value === value) {
                document.getElementById(i.toString()).classList.add(value);
            }
        });
    }
}

// Function to introduce a delay
function delay(milliseconds){
    return new Promise(resolve => {
        setTimeout(resolve, milliseconds);
    });
}

// Function to change color of an element
function change_color(id) {
    document.getElementById(id).classList.add('red');
}

// Function to change color back to default
function change_color_back(id) {
    document.getElementById(id).classList.remove('red');
}

// Function to highlight the selected word
async function pick_word(answer) {
    remove_highlight()
    const str = answer;
    const arr = JSON.parse(str);
    document.getElementById(arr[0]).classList.add('highlight_dark');
    for (let i = 1; i < (arr.length); i++) {
        await delay(150)
        document.getElementById(arr[i]).classList.add('highlight_light');
    }
}

// Function to reset input fields and classes
function reset_button() {
    const all_inputs = document.querySelectorAll('.letters_values');
    all_inputs.forEach(function (input) {
        input.value = '';
    });
    const reset_classes = document.querySelectorAll('.letters');
    reset_classes.forEach(function(reset_class) {
        reset_class.classList.remove('normal_block', 'double_letter', 'triple_letter', 'double_points');
    });
    const reset_values = document.querySelectorAll('.special_block');
    reset_values.forEach(function (reset_value) {
        reset_value.value = 'normal_block';
    });
    copy_special_block_value();
    const answer = document.querySelector('.answer');
    if (answer) {
        answer.style.display = 'none';
    }
    remove_highlight()
}

// Function to move focus to the next input field
function move_to_next_input(current_input, next_input_id) {
    const next_text_box = document.getElementsByName(next_input_id)[0];
    if (next_text_box) {
        if (current_input.value.length === 1) {
            next_text_box.focus();
        }
    }
}

// Function to handle special block selection
function special_block(element, count, event) {
    if (event.target.tagName.toLowerCase() !== 'input') {
        const classes = ['normal_block', 'double_letter', 'triple_letter', 'double_points'];
        
        for (let i = 0; i < classes.length; i++) {
            const currentClass = classes[i];
            const nextClass = classes[(i + 1) % classes.length];

            const input_name = 'special_block_' + count;
            const input = document.querySelector('input[name="' + input_name + '"]');
            
            if ((input.value === currentClass)) {
                element.classList.remove(currentClass);
                element.classList.add(nextClass);
                input.value = nextClass;
                break;
            }
        }
    }
}

// Initialization when the DOM is loaded
document.addEventListener('DOMContentLoaded', function () {
    const text_box = document.getElementsByName('1')[0];
    text_box.focus();
    copy_special_block_value();
});