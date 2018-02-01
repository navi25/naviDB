from components.row import Row;
class Table(object):
    global _data;
    _data = list();

    def insert(self,row):
        _data.append(row);

    def update(self,row, **kwargs):
        for l in _data:
            l.update(row);

    def delete(self,row):
        if row in _data:
            _data.remove(row);

    def show(self):
        print(_data)

    def purge(self):
        _data.clear();


t = Table();
d = {"name" : "navi"};
t.insert(d)
t.show()
t.update({"count" : "kittu"})
t.show()
