<template>
    <div class="container">
        <div class="DropZone2" :class="{ 'active-DropZone2': active }" @dragenter.prevent="handleDragEnter" @dragover.prevent="handleDragOver" @dragleave.prevent="handleDragLeave" @drop="handleDrop" @click="clickButton" @mouseup="handleMouseRelease">
            <form id="upload_form">
                <label id="file_input_label" for="input_file">
                    Drag and drop or click to upload a file
                    <input ref="myButtonRef" type="file" id="input_file" accept=".doc, .pdf" class="SubmitFileZoneClass">
                </label>
            </form>
        </div>
    </div>

</template>

<script>
import {
    ref
} from "vue";

export default {
    name: "DropZone2",
    setup() {
        const active = ref(false);
        const myButtonRef = ref(null);

        const toggleActive = (value) => {
            active.value = value;
        };

        const handleDragEnter = () => {
            toggleActive(true);
        };

        const handleDragOver = () => {
            event.preventDefault();
        };

        const handleDragLeave = () => {
            toggleActive(false);
        };

        const clickButton = () => {
            console.log('The div was clicked!');
            const myButton = myButtonRef.value;
            if (!myButton) {
                console.log('Failed to get the button element');
            } else {
                myButton.click();
            }
        };

        return {
            active,
            toggleActive,
            handleDragEnter,
            handleDragOver,
            handleDragLeave,
            clickButton,
            myButtonRef,
        };
    },
};
</script>

<style>
input {
    display: none;
}

.DropZone2 {
    background-color: lightblue;
    color: white;
    margin: auto;
    padding: 100px;
    font-size: 20px;
    display: flex;
    justify-content: center;
}

.active-DropZone2 {
    background-color: orange;
}
</style>
