// ./ogre/Docs/src/sm-redesign/WorldUpdate.odt
// ./raisimLib/include/raisim/World.hpp
// ./raisim_build/include/raisim/World.hpp

#include "raisim/World.hpp"
#include <iostream>

int main() {
    raisim::World world;
    // auto anymal = world.addArticulatedSystem(“pathToURDF”); // initialized to zero angles and identity orientation. Use setState() for a specific initial condition
    // auto anymal = world.setState(0,0,0);
    auto ball = world.addSphere(1, 1); // radius and mass
    auto ground = world.addGround();
    
    world.setTimeStep(0.002);
    world.integrate();

    std::cout << world.getGravity() << std::endl;
    // std::cout << ball.getPosition() << std::endl;
    // std::cout << ball.getEnergy() << std::endl;
}