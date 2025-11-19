# $NetBSD$

DISTNAME=	qtpy-2.4.3
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	python
MASTER_SITES=	${MASTER_SITE_PYPI:=Q/QtPy/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/QtPy/
COMMENT=	Abstraction layer for PyQt5/PySide2/PyQt6/PySide6
LICENSE=	mit

DEPENDS+=	${PYPKGPREFIX}-packaging>0:../../devel/py-packaging

USE_LANGUAGES=	# none

post-extract:
	${CHMOD} -R o-w,g-w ${WRKSRC}

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} qtpy qtpy-${PYVERSSUFFIX} || ${TRUE}

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
