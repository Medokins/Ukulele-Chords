import math

def frequency_to_note(freq, easier_chords=True):
    if easier_chords:
        chords = ['Am', 'A',  #A minor A major
                  'Bm', 'B',  #B minor B major
                  'Cm', 'C',  #C minor C major
                  'Dm', 'D',  #D minor D major
                  'Em', 'E',  #E minor E major
                  'Fm', 'F',  #F minor F major 
                  'Gm', 'G']  #G minor G major

    if freq == 0:
        freq = 0.001
    chord_number = 12 * math.log2(freq / 440) + 49  
    chord_number = round(chord_number)
        
    chord = (chord_number - 1 ) % len(chords)
    chord = chords[chord]
    
    octave = (chord_number + 8 ) // len(chords)
    
    return chord, octave