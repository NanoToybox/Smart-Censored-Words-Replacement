% Initialization
clear ; close all; clc

X = load("x_feat_0.txt");

% PCA
[U, S] = pca(X);

dimension = 1000;

% check variance retaining percentage, should be over 0.99
retain_perc = sum(sum(S(:,1:dimension)))/sum(sum(S));
fprintf("PCA with dimension : %i, variance retaining percentage : %d\n",dimension,retain_perc);

% Dimension Reduction
Z = projectData(X, U, dimension);




K = 6; %政治(events people organization) ads(chem guns no) sex(book) abuse  website other 
max_iters = 10;

% initialize the centroids randomly. 
initial_centroids = kMeansInitCentroids(Z, K);

% Run K-Means
[centroids, idx] = runkMeans(Z, initial_centroids, max_iters);

save out_test.txt idx
