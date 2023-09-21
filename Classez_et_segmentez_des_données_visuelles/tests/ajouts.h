#pragma once

#include <opencv2/opencv.hpp>

cv::Mat ajout_bruit(const cv::Mat& image_a_traite, const cv::Scalar& moyenne_des_bruits, const cv::Scalar& intensite_du_bruit);
