%define device yuga
%define vendor sony
%define vendor_pretty Sony
%define device_pretty Xperia Z

%define android_config \
#define QCOM_HARDWARE 1\
%{nil}

%include rpm/droid-hal-device.inc
