% Initialization
clear ; close all; clc

K = 6; %政治(events people organization) ads(chem guns no) sex(book) abuse  website other 
max_iters = 10;

% initialize the centroids randomly. 
initial_centroids = kMeansInitCentroids(Z, K);

% Run K-Means
[centroids, idx] = runkMeans(Z, initial_centroids, max_iters);

save out_test.txt idx
