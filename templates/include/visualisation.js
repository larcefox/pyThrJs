//import './js/bootstrap.js';
//import './css/bootstrap.min.css';
import * as dat from './js/dat.js';
import * as THREE from './js/three.js';
import {OrbitControls} from './js/OrbitControls.js';


let btn = document.createElement("button");
btn.innerHTML = "Reload";
btn.ClassName = "btn btn-outline-primary";
btn.id = "reload";
btn.addEventListener("click", LoadJsonData);
btn.addEventListener("click", animate);
document.body.appendChild(btn);

const scene = new THREE.Scene();
const camera = new THREE.
    PerspectiveCamera(
        75,
        innerWidth / innerHeight,
        0.1,
        1000
    )

const renderer = new THREE.WebGLRenderer()

renderer.setSize(innerWidth, innerHeight)
renderer.setPixelRatio(devicePixelRatio)
document.body.appendChild(renderer.domElement)

new OrbitControls(camera, renderer.domElement)
let geometry = []

async function LoadJsonData(){
     
    let url = 'http://10.8.0.2:9000/data';
    let response = await fetch(url);
    if (response.ok) { // if HTTP-status is 200-299
        let data = await response.json(); // read response body and parse as JSON
        console.log(data)
        // loop parse data grom canvas.py 
        for (const [key, value] of Object.entries(data)) {
            if (value.type == 'BoxGeometry') {
                const mesh = new THREE.Mesh(
                    new THREE.BoxGeometry(value.width, value.height, value.depth),
                    new THREE.MeshBasicMaterial({color: value.color}))
                console.log(value.width)
                console.log(value.id)
                scene.add(mesh)
            }
        }
    }else {
        alert("HTTP-Error: " + response.status);
    }
};

LoadJsonData();

const light1 = new THREE.DirectionalLight(
    0xffffff, 1
)
light1.position.set(0, 0, 1)

const light2 = new THREE.DirectionalLight(
    0xffffff, 1
)
light2.position.set(0, 0, -1)

scene.add(light1, light2)
camera.position.z = 20


renderer.render(scene, camera)

function animate() {
    requestAnimationFrame(animate)
    renderer.render(scene, camera)
    // mesh.rotation.x += 0.01
    // mesh.rotation.y += 0.01
    // planeMesh.rotation.z -= 0.01
    // planeMesh.rotation.x -= 0.01
}

animate()

