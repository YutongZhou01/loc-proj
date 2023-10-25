<script setup>
  // Vue 3 script setup can be added here if needed.
</script>

<template>
  <!-- Main content section -->
  <main>
    <div class="container">
      <div class="row">
        <!-- Left Column (Uploaded Files) -->
        <div class="col-9 border" style="min-height: 40em;">
          <!-- Container for displaying uploaded files -->
          <div class="container border mt-2" style="min-height: 20em;">
            <p class="fs-3 text-center">Uploaded Files</p>
          </div>

          <!-- Container displaying the current working directory -->
          <div class="container border mt-2 bg-light">
            <p class="">[Working Directory] ~/.../...</p>
          </div>

          <!-- List of uploaded files -->
          <ul class="list-group">
            <!-- List item for a file -->
            <li class="list-group-item">
              <div class="row">
                <!-- Kind of file -->
                <div class="col-2">
                  Kind
                </div>
                <!-- Name of the file -->
                <div class="col-10">
                  Name
                </div>
              </div>
            </li>
            <!-- Sample list items for uploaded files -->
            <li class="list-group-item">
              <div class="row">
                <!-- Icon indicating file type (e.g., folder) -->
                <div class="col-2">
                  <i class="bi bi-folder"></i>
                </div>
                <!-- Title of the file -->
                <div class="col-10">
                  Title
                </div>
              </div>
            </li>
            <!-- Repeat this structure for additional uploaded files -->
          </ul>
        </div>

        <!-- Right Column (File Details) -->
        <div class="col-3 border">
          <!-- Card displaying file details -->
          <div class="card border-0">
            <!-- File thumbnail -->
            <img src="../assets/Document_Icon.svg" class="img-thumbnail border-0" alt="Document Thumbnail" style="height: 300px;">
            <div class="card-body">
              <!-- File details displayed in rows -->
              <div class="mb row">
                <label for="staticEmail" class="col-sm-5 col-form-label">Name:</label>
                <div class="col-sm-7">
                  <input type="text" readonly class="form-control-plaintext fw-bold" id="staticName" value="Title 1">
                </div>
                <label for="staticAuthor" class="col-sm-5 col-form-label">Author:</label>
                <div class="col-sm-7">
                  <input type="text" readonly class="form-control-plaintext fw-bold" id="staticAuthor" value="John Doe">
                </div>
                <label for="staticAnnotated" class="col-sm-5 col-form-label">Annotated:</label>
                <div class="col-sm-7">
                  <input type="text" readonly class="form-control-plaintext fw-bold" id="staticAnnotated" value="Yes/No">
                </div>
                <label for="staticUploader" class="col-sm-5 col-form-label">Uploader:</label>
                <div class="col-sm-7">
                  <input type="text" readonly class="form-control-plaintext fw-bold" id="staticUploader" value="John Doe">
                </div>
              </div>
              <!-- You can add similar rows for Author, Annotated, and Uploader -->

            </div>

            <!-- Buttons for actions -->
            <a type="button" class="btn btn-primary btn-lg mb-3" href="/annotation">Annotate <i class="bi bi-pencil-square"></i></a>
            <a type="button" class="btn btn-primary btn-lg" href="/#">Document History <i class="bi bi-clock-history"></i></a>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
