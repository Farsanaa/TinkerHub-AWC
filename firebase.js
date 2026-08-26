// Import Firebase
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.0.0/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/12.0.0/firebase-firestore.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/12.0.0/firebase-auth.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/12.0.0/firebase-storage.js";
// Your Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBiq5jwtf7YpxPUaO7h_bda_8RixmBj1ZI",
  authDomain: "tinkerhub-awc.firebaseapp.com",
  projectId: "tinkerhub-awc",
  storageBucket: "tinkerhub-awc.firebasestorage.app",
  messagingSenderId: "883194473823",
  appId: "1:883194473823:web:865155c24a68685aaf1aea",
  measurementId: "G-RFHMBFFS45"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firestore
const db = getFirestore(app);

// Initialize Authentication
const auth = getAuth(app);

// Initialize Storage
const storage = getStorage(app);

// Export the database, authentication, and storage instances so we can use them in other files
export { db, auth, storage };