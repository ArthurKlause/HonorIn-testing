#version 450

layout (binding = 0) uniform sampler2D samplerColor;

layout(location = 0) in vec3 fragColor;

layout (location = 1) in vec2 inUV;

layout(location = 0) out vec4 outColor;

void main() {
    //outColor = vec4(fragColor, 1.0);
    //outColor = texture(samplerColor, vec2(0,0));

//    float border = 0.005f; //(has to be between 0 and 1)
//    if((inUV.s > 1-border || inUV.s < border) || (inUV.t > 1-border || inUV.t < border)){
//        outColor = vec4(fragColor, 1.0);
//    }
//    else {
//        outColor = texture(samplerColor, vec2(inUV.s, 1.0 - inUV.t));
//        if(outColor == vec4(0.0,0.2,0.2,1.0)){
//            outColor = vec4(0.0,1.0,0.0,1.0);
//        }
//    }

    outColor = texture(samplerColor, vec2(inUV.s, 1.0 - inUV.t));

}  