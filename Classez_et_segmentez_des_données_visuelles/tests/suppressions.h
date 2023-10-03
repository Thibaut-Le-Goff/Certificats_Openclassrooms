#pragma once

#include <opencv2/opencv.hpp>
#include <opencv2/core/mat.hpp>

void suppression_bruit(const cv::Mat& image_a_traite, const int& taille_matrice);