import * as dat from './js/dat.js';
import * as THREE from './js/three.js';
import {OrbitControls} from './js/OrbitControls.js';


const gui = new dat.GUI()
const world = {
    plane: {
        width: 10,
        height: 10,
        widthSegments: 10,
        heightSegments: 10,
    },
    planeColor: {
        red: 255,
        green: 0,
        blue: 0
    }
}

for ( let key in world.plane ) {
    gui.add( world.plane, key, 1, 20).
    onChange(generatePlain)
}

for ( let key in world.planeColor ) {
    gui.add( world.planeColor, key, 1, 255).
    onChange(() => {
        planeMaterial.color.setRGB(
            world.planeColor.red,
            world.planeColor.green,
            world.planeColor.blue
        )
    })
}

function generatePlain(){
    planeMesh.geometry.dispose()
    planeMesh.geometry = new THREE.PlaneGeometry(
        world.plane.width,
        world.plane.height,
        world.plane.widthSegments,
        world.plane.heightSegments)
    const { array } = planeMesh.geometry.attributes.position
    for (let i = 0; i < array.length; i += 3 ) {
        // const x = array[i]
        // const y = array[i + 1]
        const z = array[i + 2]
        array[i + 2] = z + Math.random()
    }}

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

const boxGeometry = new THREE.BoxGeometry(1, 1, 1)
const material = new THREE.MeshBasicMaterial( { color: 0x1000D0} )
const mesh = new THREE.Mesh(boxGeometry, material)
const planeGeometry = new THREE.PlaneGeometry(
    5,
    5,
    10,
    10 )
const planeMaterial = new THREE.MeshPhongMaterial( { color: 0xFF3A00,
    side: THREE.DoubleSide, flatShading: THREE.FlatShading } )
const planeMesh = new THREE.Mesh(planeGeometry, planeMaterial)

generatePlain()

const light1 = new THREE.DirectionalLight(
    0xffffff, 1
)
light1.position.set(0, 0, 1)

const light2 = new THREE.DirectionalLight(
    0xffffff, 1
)
light2.position.set(0, 0, -1)

scene.add(planeMesh, light1, light2)
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