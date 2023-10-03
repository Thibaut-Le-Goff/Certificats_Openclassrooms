#pragma once

#include <opencv2/opencv.hpp>
#include <opencv2/core/mat.hpp>
#include <opencv2/core.hpp>


cv::Mat ajout_bruit(const cv::Mat& image_a_traite, const cv::Scalar& moyenne_des_bruits, const cv::Scalar& intensite_du_bruit);
