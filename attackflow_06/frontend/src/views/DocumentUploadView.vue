<script>
import {
    ref
} from 'vue'

import DropZone2 from "../components/DropZone2.vue";

export default {
    name: "DocumentUploadView",
    components: {
        DropZone2,
    },
    setup() {
        var uploadSuccessCount = 0;
        const DropZoneFile = ref("");
        const DropZone_name = ref("");
        const data = ref(null);

        // retrieve uploaded files
        const uploadedFiles = ref([]);
        // fetch uploaded files method
        const fetchUploadedFiles = async () => {
            const response = await fetch('http://127.0.0.1:5001/get_document');
            data = await response.json();
            // modification below added to retrive files for display contents on doc_upload page
            uploadedFiles.value.fileURL = data.file_url;
            uploadedFiles.value.fileType = data.file_type;
            return {
                uploadedFiles,
                fetchUploadedFiles,
                fileURL: '',
                fileType: '',
                fContent: '',
            };
        };

        const handle_drop = (event) => {
            DropZoneFile.value = event.dataTransfer.files[0];
            DropZone_name.value = event.dataTransfer.files[0].name;
        }

        const handle_change = () => {
            const fileInput = document.querySelector('.SubmitFileZoneClass');
            DropZoneFile.value = fileInput.files[0];
            DropZone_name.value = fileInput.files[0].name;
        }
        // upload file method
        const uploadFile = () => {
            let file;
            if (DropZoneFile.value) {
                file = DropZoneFile.value;
            } else {
                file = document.querySelector('input[type="file"]').files[0];
            }
            if (file) {
                const formData = new FormData();
                formData.append('file', file);

                fetch('http://127.0.0.1:5001/upload_document', {
                    method: 'POST',
                    body: formData
                }).then(response => {
                    //console.log(response);
                    return response.json();
                }).then(response => {
                    //Pop up alert with error message
                    if(response["status"] == 'success'){
                        alert(response["msg"]);
                        //Success Upload
                        window.location.href="/annotation";
                    }else{
                        alert(response["error"]);
                    }
                    
                    
                });

            }
        };
        return {
            DropZoneFile,
            handle_drop,
            handle_change,
            DropZone_name,
            uploadFile,
            uploadSuccessCount,
            fileURL: '',
            fileType: '',
            fContent: ''
        };

    }
}
</script>

<template>
    <!-- Drop zone for file upload -->
    <div class="drop_zone_div">
      <!-- Custom component for handling file drops -->
      <DropZone2 @drop.prevent="handle_drop" @change="handle_change"></DropZone2>
  
      <!-- Display the name of the dropped file -->
      <div class="d-flex justify-content-center">
        <div class="fs-2 mb-3" id="file_name_display">file to drop: {{DropZone_name}}</div>
      </div>
  
      <!-- Button to send the uploaded file -->
      <div class="d-flex justify-content-center">
        <div>
          <button class="btn btn-primary fs-2" type="submit" value="Send_file" @click="uploadFile">
            Send file <i class="bi bi-send"></i>
          </button>
        </div>
      </div>
    </div>
  </template>
  

<style>
@media (min-width: 1024px) {
    .about {
        min-height: 100vh;
        display: flex;
        align-items: center;
    }
}
</style>
