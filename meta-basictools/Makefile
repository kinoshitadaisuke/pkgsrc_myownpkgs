# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-basictools-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs shells graphics math science python
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for basic tools
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# security
DEPENDS+=	mozilla-rootcerts-openssl>=0:../../security/mozilla-rootcerts-openssl
DEPENDS+=	openssh>=0:../../security/openssh
DEPENDS+=	openssl>=0:../../security/openssl

# shells
DEPENDS+=	tcsh>=0:../../shells/tcsh
DEPENDS+=	zsh>=0:../../shells/zsh

# archivers
DEPENDS+=	bzip2>=0:../../archivers/bzip2
DEPENDS+=	bzip3>=0:../../archivers/bzip3
DEPENDS+=	gtar>=0:../../archivers/gtar
DEPENDS+=	unzip>=0:../../archivers/unzip
DEPENDS+=	xz>=0:../../archivers/xz
DEPENDS+=	zip>=0:../../archivers/zip

# converters
DEPENDS+=	base64>=0:../../converters/base64
DEPENDS+=	dos2unix>=0:../../converters/dos2unix
#DEPENDS+=	unix2dos>=0:../../converters/unix2dos

# devel
DEPENDS+=	php-mode>=0:../../devel/php-mode

# editors
DEPENDS+=	emacs29>=0:../../editors/emacs29

# file systems
DEPENDS+=	fuse-exfat>=0:../../filesystems/fuse-exfat
DEPENDS+=	fuse-ext2>=0:../../filesystems/fuse-ext2

# fonts
DEPENDS+=	arphic-ttf>=0:../../fonts/arphic-ttf
DEPENDS+=	cyberbit-ttf>=0:../../fonts/cyberbit-ttf
DEPENDS+=	intlfonts>=0:../../fonts/intlfonts
DEPENDS+=	freefont-ttf>=0:../../fonts/freefont-ttf
DEPENDS+=	motoya-fonts>=0:../../fonts/motoya-fonts
DEPENDS+=	mozilla-fonts>=0:../../fonts/mozilla-fonts
#DEPENDS+=	noto-cjk-fonts>=0:../../fonts/noto-cjk-fonts
#DEPENDS+=	noto-fonts>=0:../../fonts/noto-fonts
DEPENDS+=	noto-ttf>=0:../../fonts/noto-ttf

# graphics
DEPENDS+=	ImageMagick>=0:../../graphics/ImageMagick
DEPENDS+=	breeze-icons>=0:../../graphics/breeze-icons
DEPENDS+=	dcraw>=0:../../graphics/dcraw
DEPENDS+=	exif>=0:../../graphics/exif
DEPENDS+=	feh>=0:../../graphics/feh
DEPENDS+=	gimp>=0:../../graphics/gimp
DEPENDS+=	gnuplot>=0:../../graphics/gnuplot
DEPENDS+=	inkscape>=0:../../graphics/inkscape
DEPENDS+=	jhead>=0:../../graphics/jhead
DEPENDS+=	netpbm>=0:../../graphics/netpbm
DEPENDS+=	oxygen-icons>=0:../../graphics/oxygen-icons
DEPENDS+=	ps2eps>=0:../../graphics/ps2eps
#DEPENDS+=	skencil>=0:../../graphics/skencil
DEPENDS+=	tgif>=0:../../graphics/tgif
DEPENDS+=	wm-icons>=0:../../graphics/wm-icons
DEPENDS+=	xfig>=0:../../graphics/xfig
DEPENDS+=	xpaint>=0:../../graphics/xpaint
DEPENDS+=	xv>=0:../../graphics/xv

# lang
DEPENDS+=	perl>=0:../../lang/perl5
DEPENDS+=	python311>=0:../../lang/python311
DEPENDS+=	python312>=0:../../lang/python312
DEPENDS+=	tcl>=0:../../lang/tcl

# meta-pkgs
DEPENDS+=	pkg_developer>=0:../../meta-pkgs/pkg_developer

# net
DEPENDS+=	openntpd>=0:../../net/openntpd
DEPENDS+=	openvpn>=0:../../net/openvpn
DEPENDS+=	rsync>=0:../../net/rsync
DEPENDS+=	tigervnc>=0:../../net/tigervnc
DEPENDS+=	wget>=0:../../net/wget
DEPENDS+=	wget2>=0:../../net/wget2
DEPENDS+=	yt-dlp>=0:../../net/yt-dlp

# print
DEPENDS+=	gv>=0:../../print/gv
DEPENDS+=	okular>=0:../../print/okular
DEPENDS+=	qpdf>=0:../../print/qpdf
DEPENDS+=	xpdf>=0:../../print/xpdf4

# sysutils
DEPENDS+=	estd>=0:../../sysutils/estd

# time
DEPENDS+=	emiclock>=0:../../time/emiclock
DEPENDS+=	oclock>=0:../../time/oclock
DEPENDS+=	xclock>=0:../../time/xclock

# wm
DEPENDS+=	fvwm3>=0:../../wm/fvwm3

# www
DEPENDS+=	curl>=0:../../www/curl

# x11
DEPENDS+=	kterm>=0:../../x11/kterm
DEPENDS+=	xdotool>=0:../../x11/xdotool
DEPENDS+=	xterm>=0:../../x11/xterm

# pkgsrc_myownpkgs
DEPENDS+=	yatex>=0:../../pkgsrc_myownpkgs/yatex-mode

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
