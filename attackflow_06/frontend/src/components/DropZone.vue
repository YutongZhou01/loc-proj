<template>
    <div @dragenter.prevent="toggleActive"
        @dragleave.prevent="toggleActive"
        @dragover.prevent
        @drop.prevent="toggleActive"
        :class="{'active-dropzone':active}"
        class="dropzone">
        <span>Drag and drop zone</span>
        <span>Or</span>
        <label for="SubmitFileZone">Select File</label>
        <input type="file" id="SubmitFileZone" class="SubmitFileZoneClass" accept=".doc, .pdf"/>
    </div>
</template>


<script>
import { ref } from "vue"; 
export default {
    name: "DropZone",
    setup(){
        const active = ref(false)
        const toggleActive = () => {
            active.value = !active.value;
        };
        return {active, toggleActive};
    }
};
</script>

<style>
.dropzone{
    width: 400px;
    height: 300px;
    display: flex;
    flex-direction: column;
    align-items: center;
    row-gap: 16px;
    border: 2px dashed blue;
    background-color: w3-light-grey; 
    tansitions: 0.1s ease all;
    label{
        padding: 10px 12px;
        background-color: w3-light-grey;
        color: w3-text-white;
        transition: .3s ease all;
    }
}
.active-dropzone{
    color: white;
    border-color: white;
    background: red;
    label{
        background-color: white;
        color: green;
    }
}
</style>