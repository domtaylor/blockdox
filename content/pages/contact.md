---
title: Contact
---
<form class="contact-form" method="post" action="/php/submit.php">
                    <div class="form-group col-md-6">
                        <input type="text" class="form-control" id="name"  name="name" placeholder="Name" required>
                    </div>
                    <div class="form-group col-md-6">
                        <input type="email" class="form-control validate email" id="email" name="email" placeholder="Enter email" required>
                    </div>
                    <p class="antispam">
                        Leave this empty:
                        <br />
                        <input name="url" />
                    </p>
                    <div class="form-group col-md-12">
                      <textarea class="form-control" rows="5" name="message" placeholder="Message" required></textarea>
                    </div>
                    <div class="form-group col-md-3 offset-md-3">
                      <button type="submit" class="btn btn-primary">Submit</button>
                    </div>
                </form>
            </div>
        </form>
