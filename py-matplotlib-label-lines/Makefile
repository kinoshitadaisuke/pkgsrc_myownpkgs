# $NetBSD$

DISTNAME=	matplotlib_label_lines-0.8.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_label_/-label-/}
CATEGORIES=	python graphics
MASTER_SITES=	${MASTER_SITE_PYPI:=m/matplotlib_label_lines/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/matplotlib_label_lines/
COMMENT=	Label line using matplotlib
LICENSE=	mit

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-more-itertools>=0:../../devel/py-more-itertools

.include "../../lang/python/wheel.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
