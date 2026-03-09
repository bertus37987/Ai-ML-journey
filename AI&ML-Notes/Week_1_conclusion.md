# Neural Networks Week1 Notizen

#### Week 1

*Was machen die Layers?*  
Die erste Layer ist meist die Input Layer, sie gibt die Rohdaten ein. Diese Daten
sind z.B. eine Zahl oder eben 784 verschiedene Pixel als Neuronen in einem Grid.
Diese werden dann weitergegeben, über die Weighted Sum, und geben wiederum den
Input für die Hidden Layers. Für die Output Layer ändert sich dann nur die
Aktivierungsfunktion.

*Was ist ein Neuron?*  
Ein Neuron kann entweder ein Input oder der Output der letzten Weighted Sum sein.
Neuronen können eine Zahl zwischen 0 und unendlich annehmen. Das liegt an der
Aktivierungsfunktion.

*Was ist ein Bias?*  
Ein Bias ist eine Zahl, die pro Neuron verschieden ist, und in der Berechnung der
Weighted Sum dazu addiert oder subtrahiert wird. Der Bias steuert, ob manche
Neuronen überhaupt oder sehr stark ausgelöst werden. Der Bias kann also manche
Neuronen schwächen oder stärken – er verschiebt die Schwelle, ab wann das Neuron
aktiviert wird.

*Was ist/macht ein Weight?*  
Ein Weight entscheidet, wie stark ein Neuron bzw. Input gewichtet werden soll.
Weights können angepasst werden, um den gewünschten Output zu erzielen. Weights
bestimmen also, wie stark ein Input gewichtet wird.

*Was macht eine Aktivierungsfunktion?*  
Eine Aktivierungsfunktion entscheidet, ob das Neuron ausgelöst wird. Heutzutage
wird meistens die ReLU verwendet. Sie passt negative Werte an – diese werden zu
null – positive Werte bleiben gleich.

# Verwendete Resourcen:  
3Blue1Brown:  But what is a neural network? | Deep learning chapter 1  
https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi
Grokking Deep Learning:
https://cdn.ttgtmedia.com/rms/pdf/grokking_deep_learning.pdf

>Autor: W.Ebert


