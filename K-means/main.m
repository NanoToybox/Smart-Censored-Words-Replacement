%% Initialization
clear ; close all; clc

X = load("x_feat_0.txt");

K = 5; 
max_iters = 50;

% initialize the centroids randomly. 
initial_centroids = kMeansInitCentroids(X, K);

% Run K-Means
[centroids, idx] = runkMeans(X, initial_centroids, max_iters);

save out_test.txt idx
