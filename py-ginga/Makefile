# $NetBSD$

DISTNAME=	ginga-4.1.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=g/ginga/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://ginga.readthedocs.io/
COMMENT=	Astronomical image viewer and toolkit
LICENSE=	modified-bsd

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-setuptools>=30.3.0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=0:../../devel/py-setuptools_scm
DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.14:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-QtPy>=2.0.1:../../pkgsrc_myownpkgs/py-qtpy
DEPENDS+=	${PYPKGPREFIX}-astropy>=3.2:../../pkgsrc_myownpkgs/py-astropy
DEPENDS+=	${PYPKGPREFIX}-Pillow>=6.2.1:../../graphics/py-Pillow
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>0:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-magic>=0.4.15:../../sysutils/py-magic
DEPENDS+=	${PYPKGPREFIX}-scipy>=0.18.1:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=2.1:../../graphics/py-matplotlib
#DEPENDS+=	opencv>=4.5.4.58:../../wip/opencv
#DEPENDS+=	${PYPKGPREFIX}-opencv-python>=4.7:../../pkgsrc_myownpkgs/py-opencv-python
#DEPENDS+=	opencv-[0-9]*:../../graphics/opencv
DEPENDS+=	${PYPKGPREFIX}-exifread>=2.3.2:../../graphics/py-exifread
DEPENDS+=	${PYPKGPREFIX}-beautifulsoup4>=4.3.2:../../www/py-beautifulsoup4
DEPENDS+=	${PYPKGPREFIX}-astroquery>=0.3.5:../../pkgsrc_myownpkgs/py-astroquery
DEPENDS+=	${PYPKGPREFIX}-docutils>=0:../../textproc/py-docutils
DEPENDS+=	${PYPKGPREFIX}-photutils>0:../../pkgsrc_myownpkgs/py-photutils
DEPENDS+=	${PYPKGPREFIX}-attrs>=19.2.0:../../devel/py-attrs
DEPENDS+=	${PYPKGPREFIX}-sphinx>=0:../../textproc/py-sphinx-astropy
DEPENDS+=	${PYPKGPREFIX}-cairo>0:../../graphics/py-cairo
DEPENDS+=	${PYPKGPREFIX}-qt5>0:../../x11/py-qt5
DEPENDS+=	${PYPKGPREFIX}-tornado>=0:../../www/py-tornado
#DEPENDS+=	${PYPKGPREFIX}-pyside>=0:../../wip/py-pyside
#DEPENDS+=	${PYPKGPREFIX}-gobject>=0:../../devel/py-gobject
DEPENDS+=	mencoder>=0:../../multimedia/mencoder
DEPENDS+=	${PYPKGPREFIX}-gwcs>=0:../../pkgsrc_myownpkgs/py-gwcs
DEPENDS+=	${PYPKGPREFIX}-asdf>=0:../../pkgsrc_myownpkgs/py-asdf
#DEPENDS+=	${PYPKGPREFIX}-piexif-[0-9]*:../../graphics/py-piexif

CHECK_INTERPRETER=	no

post-extract:
	${CHMOD} -R go-w ${WRKSRC}

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} ggrc ggrc-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} ginga ginga-${PYVERSSUFFIX} || ${TRUE}

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
