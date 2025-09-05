import pygame as py
import math
import config as cfg
import random as rn

def dashedLines(surface, start, end, color, thickness, dash_length=10, gap_length=10):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = math.sqrt(dx**2 + dy**2)
    if length == 0:
        return
    dashes = int(length / (dash_length + gap_length))
    if dashes == 0:
        py.draw.line(surface, color, start, end, thickness)
        return
    unit_x = dx / length
    unit_y = dy / length
    for i in range(dashes):
        start_x = start[0] + unit_x * i * (dash_length + gap_length)
        start_y = start[1] + unit_y * i * (dash_length + gap_length)
        end_x = start_x + unit_x * dash_length
        end_y = start_y + unit_y * dash_length
        py.draw.line(surface, color, (start_x, start_y), (end_x, end_y), thickness)

class Graph:
    def __init__(self):
        #self.points = points if points is not None else []
        self.points = [
Point((12, 676)),
Point((967, 5)),
Point((1571, -458)),
Point((1620, -543)),
Point((1634, -618)),
Point((1618, -732)),
Point((1551, -823)),
Point((1215, -1096)),
Point((1044, -1199)),
Point((879, -1235)),
Point((720, -1226)),
Point((644, -1166)),
Point((601, -1063)),
Point((595, -972)),
Point((640, -869)),
Point((658, -793)),
Point((635, -717)),
Point((536, -607)),
Point((428, -543)),
Point((292, -499)),
Point((122, -483)),
Point((-349, -514)),
Point((-800, -561)),
Point((-1149, -621)),
Point((-1403, -720)),
Point((-1735, -944)),
Point((-1875, -1122)),
Point((-1900, -1308)),
Point((-1854, -1490)),
Point((-1738, -1605)),
Point((-1598, -1646)),
Point((-1377, -1643)),
Point((-1252, -1606)),
Point((-1165, -1547)),
Point((-1084, -1431)),
Point((-1021, -1263)),
Point((-1008, -1105)),
Point((-1019, -878)),
Point((-1085, -348)),
Point((-1067, -264)),
Point((-1016, -181)),
Point((-914, -139)),
Point((-809, -133)),
Point((-637, -178)),
Point((-452, -246)),
Point((-361, -290)),
Point((-221, -309)),
Point((-88, -352)),
Point((12, -386)),
Point((204, -392)),
Point((346, -398)),
Point((451, -432)),
Point((549, -513)),
Point((663, -598)),
Point((1065, -910)),
Point((1421, -1266)),
Point((1572, -1377)),
Point((1707, -1388)),
Point((1841, -1365)),
Point((1989, -1284)),
Point((2091, -1181)),
Point((2139, -1065)),
Point((2134, -917)),
Point((2104, -764)),
Point((2025, -556)),
Point((1897, -446)),
Point((1677, -373)),
Point((1515, -267)),
Point((1370, -142)),
Point((1168, 35)),
Point((1106, 132)),
Point((1084, 300)),
Point((1129, 446)),
Point((1272, 562)),
Point((1532, 643)),
Point((1711, 612)),
Point((1889, 507)),
Point((1991, 358)),
Point((1951, 154)),
Point((1853, -5)),
Point((1729, -73)),
Point((1588, -83)),
Point((1474, -48)),
Point((1372, 22)),
Point((1262, 108)),
Point((757, 393)),
Point((663, 400)),
Point((567, 408)),
Point((483, 443)),
Point((345, 551)),
Point((189, 666)),
Point((61, 749)),
Point((3, 809)),
Point((-44, 899)),
Point((-56, 1009)),
Point((-35, 1101)),
Point((24, 1155)),
Point((124, 1181)),
Point((221, 1190)),
Point((296, 1151)),
Point((342, 1088)),
Point((356, 984)),
Point((297, 915)),
Point((182, 852)),
Point((69, 837)),
Point((-140, 830)),
Point((-294, 843)),
Point((-443, 820)),
Point((-521, 744)),
Point((-553, 643)),
Point((-538, 542)),
Point((-487, 482)),
Point((-423, 463)),
Point((-351, 458)),
Point((-277, 484)),
Point((-229, 525)),
Point((-192, 591)),
Point((-172, 638)),
Point((-107, 669))
        ]
        self.segments = [
Segment(Point((967, 5)), Point((12, 676))),
Segment(Point((1571, -458)), Point((967, 5))),
Segment(Point((1620, -543)), Point((1571, -458))),
Segment(Point((1634, -618)), Point((1620, -543))),
Segment(Point((1618, -732)), Point((1634, -618))),
Segment(Point((1551, -823)), Point((1618, -732))),
Segment(Point((1215, -1096)), Point((1551, -823))),
Segment(Point((1044, -1199)), Point((1215, -1096))),
Segment(Point((879, -1235)), Point((1044, -1199))),
Segment(Point((720, -1226)), Point((879, -1235))),
Segment(Point((644, -1166)), Point((720, -1226))),
Segment(Point((601, -1063)), Point((644, -1166))),
Segment(Point((595, -972)), Point((601, -1063))),
Segment(Point((640, -869)), Point((595, -972))),
Segment(Point((658, -793)), Point((640, -869))),
Segment(Point((635, -717)), Point((658, -793))),
Segment(Point((536, -607)), Point((635, -717))),
Segment(Point((428, -543)), Point((536, -607))),
Segment(Point((292, -499)), Point((428, -543))),
Segment(Point((122, -483)), Point((292, -499))),
Segment(Point((-349, -514)), Point((122, -483))),
Segment(Point((-800, -561)), Point((-349, -514))),
Segment(Point((-1149, -621)), Point((-800, -561))),
Segment(Point((-1403, -720)), Point((-1149, -621))),
Segment(Point((-1735, -944)), Point((-1403, -720))),
Segment(Point((-1875, -1122)), Point((-1735, -944))),
Segment(Point((-1900, -1308)), Point((-1875, -1122))),
Segment(Point((-1854, -1490)), Point((-1900, -1308))),
Segment(Point((-1738, -1605)), Point((-1854, -1490))),
Segment(Point((-1598, -1646)), Point((-1738, -1605))),
Segment(Point((-1377, -1643)), Point((-1598, -1646))),
Segment(Point((-1252, -1606)), Point((-1377, -1643))),
Segment(Point((-1165, -1547)), Point((-1252, -1606))),
Segment(Point((-1084, -1431)), Point((-1165, -1547))),
Segment(Point((-1021, -1263)), Point((-1084, -1431))),
Segment(Point((-1008, -1105)), Point((-1021, -1263))),
Segment(Point((-1019, -878)), Point((-1008, -1105))),
Segment(Point((-1085, -348)), Point((-1019, -878))),
Segment(Point((-1067, -264)), Point((-1085, -348))),
Segment(Point((-1016, -181)), Point((-1067, -264))),
Segment(Point((-914, -139)), Point((-1016, -181))),
Segment(Point((-809, -133)), Point((-914, -139))),
Segment(Point((-637, -178)), Point((-809, -133))),
Segment(Point((-452, -246)), Point((-637, -178))),
Segment(Point((-361, -290)), Point((-452, -246))),
Segment(Point((-221, -309)), Point((-361, -290))),
Segment(Point((-88, -352)), Point((-221, -309))),
Segment(Point((12, -386)), Point((-88, -352))),
Segment(Point((204, -392)), Point((12, -386))),
Segment(Point((346, -398)), Point((204, -392))),
Segment(Point((451, -432)), Point((346, -398))),
Segment(Point((549, -513)), Point((451, -432))),
Segment(Point((663, -598)), Point((549, -513))),
Segment(Point((1065, -910)), Point((663, -598))),
Segment(Point((1421, -1266)), Point((1065, -910))),
Segment(Point((1572, -1377)), Point((1421, -1266))),
Segment(Point((1707, -1388)), Point((1572, -1377))),
Segment(Point((1841, -1365)), Point((1707, -1388))),
Segment(Point((1989, -1284)), Point((1841, -1365))),
Segment(Point((2091, -1181)), Point((1989, -1284))),
Segment(Point((2139, -1065)), Point((2091, -1181))),
Segment(Point((2134, -917)), Point((2139, -1065))),
Segment(Point((2104, -764)), Point((2134, -917))),
Segment(Point((2025, -556)), Point((2104, -764))),
Segment(Point((1897, -446)), Point((2025, -556))),
Segment(Point((1677, -373)), Point((1897, -446))),
Segment(Point((1515, -267)), Point((1677, -373))),
Segment(Point((1370, -142)), Point((1515, -267))),
Segment(Point((1168, 35)), Point((1370, -142))),
Segment(Point((1106, 132)), Point((1168, 35))),
Segment(Point((1084, 300)), Point((1106, 132))),
Segment(Point((1129, 446)), Point((1084, 300))),
Segment(Point((1272, 562)), Point((1129, 446))),
Segment(Point((1532, 643)), Point((1272, 562))),
Segment(Point((1711, 612)), Point((1532, 643))),
Segment(Point((1889, 507)), Point((1711, 612))),
Segment(Point((1991, 358)), Point((1889, 507))),
Segment(Point((1951, 154)), Point((1991, 358))),
Segment(Point((1853, -5)), Point((1951, 154))),
Segment(Point((1729, -73)), Point((1853, -5))),
Segment(Point((1588, -83)), Point((1729, -73))),
Segment(Point((1474, -48)), Point((1588, -83))),
Segment(Point((1372, 22)), Point((1474, -48))),
Segment(Point((1262, 108)), Point((1372, 22))),
Segment(Point((757, 393)), Point((1262, 108))),
Segment(Point((663, 400)), Point((757, 393))),
Segment(Point((567, 408)), Point((663, 400))),
Segment(Point((483, 443)), Point((567, 408))),
Segment(Point((345, 551)), Point((483, 443))),
Segment(Point((189, 666)), Point((345, 551))),
Segment(Point((61, 749)), Point((189, 666))),
Segment(Point((3, 809)), Point((61, 749))),
Segment(Point((-44, 899)), Point((3, 809))),
Segment(Point((-56, 1009)), Point((-44, 899))),
Segment(Point((-35, 1101)), Point((-56, 1009))),
Segment(Point((24, 1155)), Point((-35, 1101))),
Segment(Point((124, 1181)), Point((24, 1155))),
Segment(Point((221, 1190)), Point((124, 1181))),
Segment(Point((296, 1151)), Point((221, 1190))),
Segment(Point((342, 1088)), Point((296, 1151))),
Segment(Point((356, 984)), Point((342, 1088))),
Segment(Point((297, 915)), Point((356, 984))),
Segment(Point((182, 852)), Point((297, 915))),
Segment(Point((69, 837)), Point((182, 852))),
Segment(Point((-140, 830)), Point((69, 837))),
Segment(Point((-294, 843)), Point((-140, 830))),
Segment(Point((-443, 820)), Point((-294, 843))),
Segment(Point((-521, 744)), Point((-443, 820))),
Segment(Point((-553, 643)), Point((-521, 744))),
Segment(Point((-538, 542)), Point((-553, 643))),
Segment(Point((-487, 482)), Point((-538, 542))),
Segment(Point((-423, 463)), Point((-487, 482))),
Segment(Point((-351, 458)), Point((-423, 463))),
Segment(Point((-277, 484)), Point((-351, 458))),
Segment(Point((-229, 525)), Point((-277, 484))),
Segment(Point((-192, 591)), Point((-229, 525))),
Segment(Point((-172, 638)), Point((-192, 591))),
Segment(Point((-107, 669)), Point((-172, 638))),
Segment(Point((-107, 669)), Point((12, 676)))
        ]
        self.delay = 20
        self.interval = self.delay
        self.temp = None
        self.dirty = True
        self.virtual_surface = py.Surface((cfg.WIDTH, cfg.HEIGHT))

    def update(self):
        keys = cfg.KEYS()
        if keys[py.K_SPACE] and self.interval == 0:
            self.interval = self.delay
            pos = cfg.MOUSE()
            # Prevent points too close together
            if not any(abs(p.x - pos[0]) < 10 and abs(p.y - pos[1]) < 10 for p in self.points):
                self.points.append(Point(pos))
                self.dirty = True

        n = len(self.points)
        if n > 1:
            seg = Segment(self.points[-1], self.points[-2] if self.temp is None else self.temp)
            self.temp = None
            if not any(s.point1 == seg.point1 and s.point2 == seg.point2 for s in self.segments):
                self.segments.append(seg)
                self.dirty = True
                
        self.temp = None
        if keys[py.K_f]:
            pos = cfg.MOUSE()
            for p in self.points:
                if abs(p.x - pos[0]) < 10 and abs(p.y - pos[1]) < 10:
                    self.temp = p
                    break

        if self.interval > 0:
            self.interval -= 1

        if cfg.offsets_changed:
            self.dirty = True
            cfg.offsets_changed = False

        self.draw()

    def draw(self):
        if self.dirty:
            self.virtual_surface.fill(cfg.BACKGROUND)
            for point in self.points:
                point.draw(self.virtual_surface)
            for segment in self.segments:
                segment.draw(self.virtual_surface)
            self.dirty = False

        cfg.screen.blit(self.virtual_surface, (0, 0))
    
    def print(self):
        print('[')
        for p in self.points:
            p.print()
            print(',')
        print(']')

        print('[')
        for s in self.segments:
            s.print()
            print(',')
        print(']')

class Point:
    def __init__(self, pos, color=(150, 150, 150)):
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.pointsRadius = 27
        self.offset_x = 0
        self.offset_y = 0

    def draw(self, surface):
        py.draw.circle(surface, self.color, (self.x + cfg.ofx, self.y + cfg.ofy), self.pointsRadius)
        py.draw.circle(surface, cfg.WHITE, (self.x + cfg.ofx, self.y + cfg.ofy), self.pointsRadius, 3)
    
    def print(self):
        print(f'Point(({self.x}, {self.y}))', end="")

    def get(self):
        self.offset_x = rn.randint(-4, 4)
        self.offset_y = rn.randint(-4, 4)
        return (self.x + self.offset_x, self.y + self.offset_y)
    
    def points(self):
        return (self.x, self.y)
    
class Segment:
    def __init__(self, point1, point2, width=51):
        self.point1 = point1
        self.point2 = point2
        self.width = width
        self.roadColor = (150, 150, 150)
        self.c1 = self.c2 = self.c3 = self.c4 = None
        self.last_ofx = self.last_ofy = None
        self.update_corners()

    def update_corners(self):
        dx = self.point2.x - self.point1.x
        dy = self.point2.y - self.point1.y
        length = math.sqrt(dx**2 + dy**2)
        if length == 0:
            self.c1 = self.c2 = self.c3 = self.c4 = (0, 0)
            return
        px = -dy / length
        py = dx / length
        half_width = self.width / 2.0
        ox = px * half_width
        oy = py * half_width
        self.c1 = (self.point1.x + ox, self.point1.y + oy)
        self.c2 = (self.point1.x - ox, self.point1.y - oy)
        self.c3 = (self.point2.x - ox, self.point2.y - oy)
        self.c4 = (self.point2.x + ox, self.point2.y + oy)
        self.last_ofx = cfg.ofx
        self.last_ofy = cfg.ofy

    def draw(self, surface):
        if self.last_ofx != cfg.ofx or self.last_ofy != cfg.ofy:
            self.update_corners()
        offset_c1 = (self.c1[0] + cfg.ofx, self.c1[1] + cfg.ofy)
        offset_c2 = (self.c2[0] + cfg.ofx, self.c2[1] + cfg.ofy)
        offset_c3 = (self.c3[0] + cfg.ofx, self.c3[1] + cfg.ofy)
        offset_c4 = (self.c4[0] + cfg.ofx, self.c4[1] + cfg.ofy)
        # Use lines instead of filled polygon
        py.draw.polygon(surface, self.roadColor, [offset_c2, offset_c3, offset_c4, offset_c1])
        py.draw.lines(surface, self.roadColor, True, [offset_c2, offset_c3, offset_c4, offset_c1], 2)
        py.draw.line(surface, cfg.WHITE, offset_c1, offset_c4, 3)
        py.draw.line(surface, cfg.WHITE, offset_c2, offset_c3, 3)
        dashedLines(surface, (self.point1.x + cfg.ofx, self.point1.y + cfg.ofy), (self.point2.x + cfg.ofx, self.point2.y + cfg.ofy), cfg.WHITE, 2)
    
    def print(self):
        print('Segment(', end="")
        self.point1.print() 
        print(', ', end="")
        self.point2.print()
        print(')', end="")