% Initialization
clear ; close all; clc

K = 6; %政治(events people organization) ads(chem guns no) sex(book) abuse  website other 
max_iters = 10;

X = load("input/PCA_training_set.txt").Z;

% initialize the centroids randomly. 
initial_centroids = kMeansInitCentroids(X, K);

% Run K-Means
[centroids, idx] = runkMeans(X, initial_centroids, max_iters);

save "output/out_test.txt" idx
save "output/centroids.txt" centroids