// AI Background Animation
const canvas = document.getElementById('ai-background');
const ctx = canvas.getContext('2d');

let width, height;
let particles = [];
let connections = [];

function resizeCanvas() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
}

class Particle {
    constructor() {
        this.x = Math.random() * width;
        this.y = Math.random() * height;
        this.vx = (Math.random() - 0.5) * 2;
        this.vy = (Math.random() - 0.5) * 2;
        this.radius = Math.random() * 3 + 1;
        this.opacity = Math.random() * 0.5 + 0.2;
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;

        if (this.x < 0 || this.x > width) this.vx *= -1;
        if (this.y < 0 || this.y > height) this.vy *= -1;

        this.x = Math.max(0, Math.min(width, this.x));
        this.y = Math.max(0, Math.min(height, this.y));
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(0, 170, 255, ${this.opacity})`;
        ctx.fill();
    }
}

function createParticles() {
    particles = [];
    const numParticles = Math.min(50, Math.floor((width * height) / 20000));
    for (let i = 0; i < numParticles; i++) {
        particles.push(new Particle());
    }
}

function drawConnections() {
    ctx.strokeStyle = 'rgba(0, 170, 255, 0.1)';
    ctx.lineWidth = 1;

    for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
            const dx = particles[i].x - particles[j].x;
            const dy = particles[i].y - particles[j].y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < 150) {
                const opacity = (150 - distance) / 150 * 0.1;
                ctx.strokeStyle = `rgba(0, 170, 255, ${opacity})`;
                ctx.beginPath();
                ctx.moveTo(particles[i].x, particles[i].y);
                ctx.lineTo(particles[j].x, particles[j].y);
                ctx.stroke();
            }
        }
    }
}

function animate() {
    ctx.clearRect(0, 0, width, height);
    
    particles.forEach(particle => {
        particle.update();
        particle.draw();
    });
    
    drawConnections();
    requestAnimationFrame(animate);
}

// Initialize
resizeCanvas();
createParticles();
animate();

// Handle window resize
window.addEventListener('resize', () => {
    resizeCanvas();
    createParticles();
});
