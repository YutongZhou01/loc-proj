import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import AttackflowView from '../views/AttackFlowView.vue'
import AnnotationView from '../views/DocumentAnnotationView.vue'
import UploadView from '../views/DocumentUploadView.vue'
import UserAuthView from '../views/UserAuthView.vue'

// Create a router instance
const router = createRouter({
  // Use createWebHistory for HTML5 History mode
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // Define routes with descriptive names
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'About',
      component: AboutView
    },
    {
      path: '/attackflow',
      name: 'Attackflow',
      component: AttackflowView
    },
    {
      path: '/annotation',
      name: 'DocumentAnnotation',
      component: AnnotationView
    },
    {
      path: '/upload',
      name: 'DocumentUpload',
      component: UploadView
    },
    {
      path: '/user',
      name: 'UserAuth',
      component: UserAuthView
    },
  ]
})

export default router
