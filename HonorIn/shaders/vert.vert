#version 450

layout(location = 0) out vec3 fragColor;

layout (location = 1) out vec2 outUV;

//vec2 positions[3] = vec2[](
//    vec2(-1.0, -1.0),
//    vec2(1.0, 1.0),
//    vec2(-1.0, 1.0)
//);

vec2 positions[6] = vec2[](
    vec2(-1.0, -1.0),
    vec2(1.0, 1.0),
    vec2(-1.0, 1.0),
    vec2(-1.0, -1.0),
    vec2(1.0, -1.0),
    vec2(1.0, 1.0)
);

//vec3 colors[3] = vec3[](
//    vec3(1.0, 0.0, 0.0),
//    vec3(0.0, 1.0, 0.0),
//    vec3(0.0, 0.0, 1.0)
//);

vec3 colors[6] = vec3[](
    vec3(1.0, 0.0, 0.0),
    vec3(0.0, 1.0, 0.0),
    vec3(0.0, 0.0, 1.0),
    vec3(1.0, 0.0, 0.0),
    vec3(1.0, 1.0, 0.0),
    vec3(0.0, 1.0, 0.0)
);

void main() {
	//outUV = vec2((gl_VertexIndex << 1) & 2, gl_VertexIndex & 2);
	outUV = 0.5*vec2(1+positions[gl_VertexIndex].x,1+positions[gl_VertexIndex].y);

    gl_Position = vec4(positions[gl_VertexIndex], 0.0, 1.0);
    fragColor = colors[gl_VertexIndex];
} 