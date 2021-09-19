def classical_work_string(rr):
    rrstring = rr.Composers.first_name + " " + rr.Composers.last_name + ": " \
             + rr.Works.title \
             + (", "  + rr.Works.opus_no if rr.Works.opus_no is not None else "") + " " \
             + ("No. " + str(rr.Works.work_no) if rr.Works.work_no is not None else "")
             
    return rrstring