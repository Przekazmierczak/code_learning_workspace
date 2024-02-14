document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  let compose_status = "new";
  document.querySelector('#compose').addEventListener('click', () => compose_email(compose_status));

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email(compose_status, reply_recipients, reply_subject, reply_body) {

  // Title
  if (compose_status === "reply") {
    document.querySelector(".compose-title").innerHTML = "Reply";
  } else {
    document.querySelector(".compose-title").innerHTML = "New Email";
  }

  
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  // Fill reply
  if (compose_status === "reply") {
    document.querySelector('#compose-recipients').value = reply_recipients;
    document.querySelector('#compose-subject').value = reply_subject;
    document.querySelector('#compose-body').value = reply_body;
  }

  // Submit button
  document.querySelector('#compose-form').onsubmit = function() {
    const compose_recipients = document.querySelector('#compose-recipients').value;
    const compose_subject = document.querySelector('#compose-subject').value;
    const compose_body = document.querySelector('#compose-body').value;
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: compose_recipients,
          subject: compose_subject,
          body: compose_body
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
    });
  }
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox title
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  if (mailbox === "inbox") {
    fetchEmail('/emails/inbox')
  } else if (mailbox === "sent") {
    fetchEmail('/emails/sent')
  } else {
    fetchEmail('/emails/archive')
  };

}

function fetchEmail(mailbox) {
  fetch(mailbox)
  .then(response => response.json())
  .then(emails => {
  // Print emails
    console.log(emails);
  
    emails.forEach((element) => {
      const id = element["id"];
      let read = element["read"];
      if (read === true) {
        read = "read_mail"
      } else {
        read = "unread_mail"
      };
      // Shows mails in html
      document.querySelector('#emails-view').innerHTML += `
      <div class="mail ${read}" data-id="${id}">
      <table>
      <tr>
      <td>Subject: ${element["subject"]}</td>
      <td>From: ${element["sender"]}</td>
      <td>Date: ${element["timestamp"]}</td>
      </tr>
      </table>
      </div>`;
    });
    document.querySelectorAll('.mail').forEach(item => {
      const id = item.dataset.id;
      item.addEventListener('click', () => load_mail(id, mailbox));
    });
  });
}

function load_mail(id, mailbox) {
  // Show the mail and hide other views
  document.querySelector('#email-view').style.display = 'block';
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
    // Show email
    console.log(email);
    document.querySelector('#email-view').innerHTML = `
    <div>From: 
    <table><tr>
    <td>${email["sender"]}</td>
    </tr></table>
    To: 
    <table><tr>
    <td>${email["recipients"]}</td>
    </tr></table>
    Date:
    <table><tr>
    <td>${email["timestamp"]}</td>
    </tr></table>
    Subject: 
    <table><tr>
    <td>${email["subject"]}</td>
    </tr></table>
    Message:
    <table><tr id="message">
    <td>${email["body"]}</td>
    </tr></table></div>`
    // Change email to read
    if (email["read"] === false) {
      fetch(`/emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
          read: true
        })
      })
    }
    // Archive button
    let archive;
    if (email["archived"] === false) {
      archive = "Archive";
    } else {
      archive = "Unarchive";
    }
    if ((mailbox === "/emails/inbox") || (mailbox === "/emails/archive")) {
      document.querySelector('#email-view').innerHTML += `<button class="btn btn-sm btn-outline-primary" id="archive_button">${archive}</button>`;
    }
    // Reply button
    document.querySelector('#email-view').innerHTML += `<br><button class="btn btn-sm btn-outline-primary" id="reply_button">Reply</button>`;
    let compose_status = "reply";
    let reply_recipients = email["sender"];
    let reply_subject;
    if (email["subject"].startsWith("Re: ")) {
      reply_subject = email["subject"]
    } else {
      reply_subject = `Re: ${email["subject"]}`
    }
    // Archive button listener
    document.querySelector('#archive_button').addEventListener('click', () => change_achive(id, email["archived"]));
    document.querySelector('#archive_button').addEventListener('click', () => load_mailbox("inbox"));
    // Reply button listener
    let reply_body = `\nOn ${email["timestamp"]} ${email["sender"]} wrote:\n${email["body"]}`;
    document.querySelector('#reply_button').addEventListener('click', () => compose_email(compose_status, reply_recipients, reply_subject, reply_body));
  });
}

function change_achive(id, status) {
  if (status === true) {
    status = false
  } else {
    status = true
  };
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
        archived: status
    })
  })
}
