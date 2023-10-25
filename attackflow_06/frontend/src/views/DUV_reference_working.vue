<script>
import {
    ref
} from 'vue'
import DropZone from "../components/DropZone.vue";
export default {
    name: "DocumentUploadView",
    components: {
        DropZone,
    },
    setup() {
        var uploadSuccessCount = 0;
        const DropZoneFile = ref("");
        const Array_Of_File_Names = ref([]);

        // retrieve uploaded files
        const uploadedFiles = ref([]);
        // fetch uploaded files method
        const fetchUploadedFiles = async () => {
            const response = await fetch('http://127.0.0.1:5001/get_document');
            const data = await response.json();
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

        const drop = (event) => {
            DropZoneFile.value = event.dataTransfer.files[0];
            Array_Of_File_Names.value = [...event.dataTransfer.files];
        }
        const selected_file = () => {
            const fileInput = document.querySelector('.SubmitFileZoneClass');
            if (fileInput.files.length > 0) {
                DropZoneFile.value = fileInput.files[0];
                Array_Of_File_Names.value = [...fileInput.files];
            }
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
                    console.log(response);
                    if (response.ok) {
                        //Success Upload
                        fetchUploadedFiles(data.file_id);
                    } else {
                        //Failed Upload
                        return response.json();
                    }
                }).then(response => {
                    //Pop up alert with error message
                    alert(response["error"]);
                });
            }
        };
        return {
            DropZoneFile,
            drop,
            selected_file,
            Array_Of_File_Names,
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
<div class="document">
    <h1>This is document upload page.</h1>
    <div class="SubmitFile">
        <DropZone @drop.prevent="drop" @change="selected_file" />
        <span class="file-info"> Files to upload: </span>
        <ul class="file-info">
            <li v-for="item in Array_Of_File_Names" :key="item.name ">
                File: {{ item.name }}
            </li>
        </ul>
        <!-- <br>
      <button @click="uploadFile">Upload</button> -->
    </div>
    <div class="upload_box">
        <p>Or Upload documents here</p>
        <form v-on:submit.prevent="onSubmit">
            <input type="file" ref="fileInput" @change="uploadFile" />
            <button @click="uploadFile">Upload</button>
        </form>
        <!-- div below display pdf contents -->
        <div>
            <iframe v-if="fileType === 'application/pdf'" :src="fileURL" width="700" height="600"></iframe>
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

<!-- old version below -->
<!-- old version below -->
<!-- old version below -->

<!-- <template>
    <div class="upload_box">
      <p>Upload documents here</p>
        <form>
          <input type="file" ref="fileInput" @change="uploadFile"/>
          <button @click="uploadFile">Upload</button>
        </form>
      </div>
  
</template>

  <script>
  // define a route called upload_document in a method called uploadFile to send a POST request to app.py to achieve file uploads
  export default {
    methods: {
      uploadFile() {
        const file = this.$refs.fileInput.files[0]
        const formData = new FormData()
        formData.append('file', file)

        fetch('http://127.0.0.1:5001/upload_document', {
          method: 'POST',
          body: formData
        }).then(response => {
          console.log(response)
        })
      }
    }
  }
  </script>

  <style>
  @media (min-width: 1024px) {
    .about {
      min-height: 100vh;
      display: flex;
      align-items: center;
    }
  }
 <style>
<style>
 </style>
</style><style>
</style>
</style> -->
