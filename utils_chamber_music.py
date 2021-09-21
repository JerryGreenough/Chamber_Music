def classical_work_string(rr):
    rrstring = rr.composers.first_name + " " + rr.composers.last_name + ": " \
             + rr.works.title \
             + (", "  + rr.works.opus_no if rr.works.opus_no is not None else "") + " " \
             + ("No. " + str(rr.works.work_no) if rr.works.work_no is not None else "")
             
    return rrstring