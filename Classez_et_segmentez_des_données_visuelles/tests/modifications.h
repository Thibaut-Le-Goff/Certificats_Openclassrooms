#pragma once

#include <opencv2/opencv.hpp>
#include <opencv2/core/mat.hpp>

cv::Mat rotation(const cv::Mat& image_a_traite, const cv::Point2f& point_de_rotation, const double& angle_de_rotation, const float& mise_a_echelle);
