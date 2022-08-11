import * as dat from './js/dat.js';
import * as THREE from './js/three.js';
import {OrbitControls} from './js/OrbitControls.js';


const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
        75,
        innerWidth / innerHeight,
        0.1,
        1000
    )

const renderer = new THREE.WebGLRenderer()
document.getElementById('control').width = 38
renderer.setSize(innerWidth, innerHeight - document.getElementById('control').width)
renderer.setPixelRatio(devicePixelRatio)
document.getElementById("app").appendChild(renderer.domElement)
new OrbitControls(camera, renderer.domElement)


// create objects from json
function LoadObjects(data){
    // draw all objects from source
    for (const [key, value] of Object.entries(data)) {
        // draw color or texture
        if ('texture' in value.material){
            var material = new THREE[value.material_type]({ map: new THREE.TextureLoader().load(value.material.texture) });
        }else{
            var material = new THREE[value.material_type](value.material);
        }

        const figure = new THREE[value.geometry_type](...Object.values(value.geometry));
        const mesh = new THREE.Mesh(figure, material);

        mesh.name = key;
        scene.add(mesh);

        // add mesh position
        mesh.position.set(...Object.values(value.position));

        // add mesh rotation
        mesh.rotation.set(...Object.values(value.rotation));

    }
    console.log(scene);
}

LoadObjects({{ data }})
document.getElementById("refresh").onclick = function () {LoadObjects({{ data }})}

const light1 = new THREE.DirectionalLight(
    0xffffff, 1
)
light1.position.set(0, 0, 1)

const light2 = new THREE.DirectionalLight(
    0xffffff, 1
)
light2.position.set(0, 0, -1)

scene.add(light1, light2)
camera.position.z = 40
camera.position.y = 40
camera.rotation.x = -40

function animate() {
     requestAnimationFrame(animate);
     //scene.getObjectByName( "Object1", true  ).rotation.x += 0.01;
     //scene.getObjectByName( "Object2", true  ).rotation.z += 0.01;
     //console.log(scene.getObjectByName("Object2").rotation.z)
     //scene.getObjectByName( "Object3", true  ).rotation.z += 0.01;
     renderer.render(scene, camera);
}

animate()

