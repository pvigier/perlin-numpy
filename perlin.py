import numpy as np

def generate_2d_perlin(shape, res, octaves=1, persistance=0.5):
    def f(t):
        return 6*t**5 - 15*t**4 + 10*t**3
    
    noise = np.zeros(shape)
    delta = (res[0]/shape[0], res[1]/shape[1])
    coordinates = np.mgrid[0:res[0]:delta[0],0:res[1]:delta[1]].transpose(1, 2, 0)
    k = 1
    amplitude = 1
    for _ in range(octaves):
        d = (shape[0] // (k*res[0]), shape[1] // (k*res[1]))
        grid = (coordinates * k) % 1
        # Gradients
        angles = 2*np.pi*np.random.rand(k*res[0]+1, k*res[1]+1)
        gradients = np.sqrt(2)*np.dstack((np.cos(angles), np.sin(angles)))
        g00 = gradients[0:-1,0:-1].repeat(d[0], 0).repeat(d[1], 1)
        g10 = gradients[1:,0:-1].repeat(d[0], 0).repeat(d[1], 1)
        g01 = gradients[0:-1,1:].repeat(d[0], 0).repeat(d[1], 1)
        g11 = gradients[1:,1:].repeat(d[0], 0).repeat(d[1], 1)
        # Ramps
        n00 = np.sum(grid * g00, 2)
        n10 = np.sum(np.dstack((grid[:,:,0]-1, grid[:,:,1])) * g10, 2)
        n01 = np.sum(np.dstack((grid[:,:,0], grid[:,:,1]-1)) * g01, 2)
        n11 = np.sum(np.dstack((grid[:,:,0]-1, grid[:,:,1]-1)) * g11, 2)
        # Interpolation
        t = f(grid)
        n0 = n00*(1-t[:,:,0]) + t[:,:,0]*n10
        n1 = n01*(1-t[:,:,0]) + t[:,:,0]*n11
        noise += amplitude * ((1-t[:,:,1])*n0 + t[:,:,1]*n1)
        # Update
        k *= 2
        amplitude *= persistance
        
    return noise
    
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    #np.random.seed(0)
    noise = generate_2d_perlin((256, 256), (4, 4), 6)
    plt.imshow(noise, cmap='gray', interpolation='lanczos')
    plt.colorbar()
    plt.show()
