<template>
  <!-- Start of the main content section -->
  <section class="vh-100 gradient-custom">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <!-- Card element for login -->
          <div class="card bg-light" style="border-radius: 1rem;">
            <div class="card-body p-5 text-center">
              <!-- User icon -->
              <div class="text-center">
                <img src="../assets/User_Icon.svg" class="rounded" alt="User Icon">
              </div>

              <!-- Login form -->
              <div class="mb-md-5 mt-md-4 pb-5">
                <!-- Username input field -->
                <div class="form-outline form-white mb-4">
                  <input type="text" id="usernameInput" class="form-control form-control-lg" placeholder="Username" />
                </div>

                <!-- Password input field -->
                <div class="form-outline form-white mb-4">
                  <input type="password" id="passwordInput" class="form-control form-control-lg" placeholder="Password" />
                </div>

                <!-- Login button -->
                <button class="btn btn-outline-dark btn-lg px-5" type="submit">Login</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- End of the main content section -->
</template>

<style scoped>
  /* Add your scoped CSS styles here if needed */
</style>
