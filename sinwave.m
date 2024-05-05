clc
clear all
close all
t=0:0.01:1
F1=4
x1=sin(2*pi*F1*t)
plot(t,x1)
xlabel("time")
ylabel("amplitude")
title("sinwave")