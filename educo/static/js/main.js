import '@/css/main.css';
import {sayHello} from './important.js';
import 'flowbite';
import htmx from 'htmx.org';
import 'htmx-ext-preload'; 
import Alpine from 'alpinejs'
 
window.Alpine = Alpine
 
Alpine.start()

console.log("Hello from main.js!");
sayHello("World!");
window.htmx = htmx; 
// window.preload = preload;

