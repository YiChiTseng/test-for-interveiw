Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}

 
>>> def test(d):
    import json
    for k in d.keys():
        d2 = d[k]
        for k2 in d2.keys():
            d3 = d2[k2]
            for k3 in d3.keys():
                d4 = d3[k3]
                for k4 in d4.keys():
                    k4 = k4
                    for v in d4.values():
                        v = v
    output_value={}
    output_value[v]= {}
    output_value[v][k4]= {}
    output_value[v][k4][k3]= {}
    output_value[v][k4][k3][k2]= {}
    output_value[v][k4][k3][k2]= k
    print("output_value =" ,  json.dumps(output_value,sort_keys=True, indent=4))

>>> 
>>> 
>>> test(input_value)
output_value = {
    "I": {
        "deserve": {
            "to": {
                "be": "hired"
            }
        }
    }
}
>>> 