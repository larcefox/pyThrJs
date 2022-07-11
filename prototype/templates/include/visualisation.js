import * as dat from './js/dat.js';
import * as THREE from './js/three.js';
import {OrbitControls} from './js/OrbitControls.js';

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

let url = 'http://0.0.0.0:8000/data';
let response = await fetch(url);
if (response.ok) { // if HTTP-status is 200-299
    let data = await response.json(); // read response body and parse as JSON
    console.log(data)

    if (Object.keys(data)[0] == 'BoxGeometry') {
        const mesh = new THREE.Mesh(
            new THREE.BoxGeometry(data.BoxGeometry.width, data.BoxGeometry.height, data.BoxGeometry.depth),
            new THREE.MeshBasicMaterial({color: data.BoxGeometry.color}))
        console.log(data.BoxGeometry.width)
        console.log(data.BoxGeometry.id)
        scene.add(mesh)
    }
}else {
    alert("HTTP-Error: " + response.status);
}

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

